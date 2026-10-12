# Research References

**Access date:** 2026-10-11

Research focused on the actual technologies and risk patterns found in this repository rather than generic best-practice lists. Findings were used as implementation guidance; tests were mocked where external state could otherwise be changed.

## Server-side request forgery and crawler destinations

### OWASP — Server-Side Request Forgery Prevention Cheat Sheet
URL: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html  
Type: Security guidance  
Relevant finding: URL validation alone and hostname allowlisting are not sufficient if redirects or DNS rebinding can direct a request to a private address; the actual connected destination must remain within the policy.  
Project implication: added scheme/credential/private-address validation, disabled automatic redirects in the audited crawler clients, and restricted sitemap fetching to same-origin URLs. The report retains DNS rebinding as a residual risk because connection-time IP pinning is not implemented.

## CSRF and browser-origin validation

### OWASP — Cross-Site Request Forgery Prevention Cheat Sheet
URL: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html  
Type: Security guidance  
Relevant finding: validate request origins for browser mutations and do not treat opaque `Origin: null` as trusted.  
Project implication: strict origin parsing, loopback checks in local mode, validated preflight methods/headers, same-origin requirements for remote mutations, and rejection of explicit cross-site browser Fetch Metadata were implemented. Full middleware runtime tests remain blocked by missing application dependencies.

## Remote studio authentication

### FastAPI — HTTP Basic Auth
URL: https://fastapi.tiangolo.com/advanced/security/http-basic-auth/  
Type: Official framework documentation  
Relevant finding: Basic authentication transports username/password in an Authorization header, and standard clients expect a 401 plus `WWW-Authenticate` challenge when credentials are missing. Basic authentication must be carried over HTTPS to protect the credentials.  
Project implication: remote studio mode now requires non-empty configured credentials and returns a 401 challenge on invalid credentials. README and `.env.example` explicitly require HTTPS termination at a trusted reverse proxy/tunnel; the application does not itself provision TLS.

## Secrets and logging

### OWASP — Secrets Management Cheat Sheet
URL: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html  
Type: Security guidance  
Relevant finding: secrets should be access-limited, rotated, revocable, and not emitted in logs; applications should make secret detection and rotation procedures explicit.  
Project implication: the actual `.env` is not included in the delivered ZIP, and the audit recommends rotating any real credentials if the original archive has crossed a trusted boundary.

### OWASP — Logging Cheat Sheet
URL: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html  
Type: Security guidance  
Relevant finding: access tokens, passwords, connection strings and other primary secrets should generally be removed, masked, hashed or otherwise protected from logs.  
Project implication: changed publishing-check and CMS error paths log the hostname/exception type rather than entire URLs or full exception content that may contain signed parameters.

## GitHub content and pull-request APIs

### GitHub REST API — Git References
URL: https://docs.github.com/en/rest/git/refs  
Type: Official API documentation  
Relevant finding: reference creation requires an explicit fully qualified `refs/heads/...` value and commit SHA; successful creation returns HTTP 201. Current docs include the `X-GitHub-Api-Version: 2026-03-10` header.  
Project implication: headless staging now looks up the base ref, creates/reuses a content branch, and only treats the branch as staged after the relevant API operations are confirmed.

### GitHub REST API — Repository Contents
URL: https://docs.github.com/en/rest/repos/contents  
Type: Official API documentation  
Relevant finding: creating/updating repository files uses Base64-encoded content; updates require the current file SHA, and fine-grained tokens need Contents write permission. The API returns success status codes such as 200/201.  
Project implication: article and optional local-media files are committed to the branch through the Contents API, file updates include the existing SHA, local media is size-limited, and path components are validated.

### GitHub REST API — Pull Requests
URL: https://docs.github.com/en/rest/pulls/pulls?apiVersion=2026-03-10  
Type: Official API documentation  
Relevant finding: the pull-request creation endpoint accepts a `draft` Boolean and returns a created PR representation after successful request processing.  
Project implication: the adapter checks for an existing open PR, creates a draft PR by default after branch/content commits, and reports success only when it receives a valid GitHub PR URL. The PR body asks reviewers to validate factual claims, source links, licensing and rendering; it no longer asserts a universal external “standard” was complied with.

## Research limitations

- No live credentials were used to verify CMS-specific API variations or GitHub permissions.
- API version headers and endpoints were checked against official documentation available at the access date, but the GitHub flow has only been validated with mocked responses in this environment.
- Third-party product/provider compatibility should be confirmed using the real staging account and a clean dependency installation before production deployment.
