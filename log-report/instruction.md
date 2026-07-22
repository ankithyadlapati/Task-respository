There's an Apache-style access log at /app/access.log. Each non-blank line has
the form:

<client_ip> - - [<timestamp>] "<METHOD> <path> HTTP/1.1" <status> <bytes>

Parse the log and write a summary report to /app/report.json as a single JSON
object with exactly these keys:

- "total_requests": integer, the number of non-blank lines in the log
- "unique_ips": integer, the number of distinct client IP addresses (the
  first field of each line)
- "top_path": string, the request path (the second token inside the quoted
  request, e.g. "/index.html") that appears most often across all requests

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. "total_requests" equals the number of non-blank lines in /app/access.log.
3. "unique_ips" equals the count of distinct client IP addresses in the log.
4. "top_path" equals the single most frequently requested path in the log.
