# Mission 7 — How computers communicate

## 1. Task / objective

Explain basic networking concepts, check HTTPS connectivity and DNS resolution, and trace how a browser opens a website.

## 2. Work completed

Sent an HTTPS HEAD request to `example.com` and looked up the domain's IPv4 address records. The selected response status and public DNS answers are saved in the mission evidence file.

## 3. Commands / tools used

`curl --head` requested response headers and reported the HTTP status after connecting over HTTPS. `dig +short example.com A` asked DNS for IPv4 address records. The evidence contains the status and the public answer addresses only.

## 4. My understanding

### 7.1 Network concepts

| Concept | Explanation | Example |
| --- | --- | --- |
| LAN | Links devices within a small area. | A school's computer lab network. |
| MAN | Connects networks across a metropolitan area. | A city network linking public library branches. |
| WAN | Connects networks across large distances. | A company's network linking offices in different countries. |
| DNS | Looks up records for domain names, including addresses. | Resolving `example.com` to IPv4 addresses. |
| Router | Forwards packets from one network to another. | A home router forwards internet traffic between the home network and the internet provider. |
| Protocol | Defines rules for messages exchanged by devices. | HTTP defines web requests and responses. |
| Packet switching | Breaks traffic into packets that routers can forward across shared links. | Packets carrying different users' website traffic can share the same link. |
| Client-server | A client requests a service that a server provides. | A browser requests a page from a web server. |

### 7.2 Connectivity and DNS observations

The HTTPS test helps check that the computer can reach the web service and receive an HTTP response. A DNS lookup shows the records returned for a requested name and record type. When a browser needs a fresh address for a site, DNS helps it find where to send the connection. A domain can have multiple addresses, and its answers can change.

### 7.3 How a website opens

1. The browser acts as the client and reads the URL to identify the domain, scheme and path.
2. It uses a cached address or asks a DNS resolver for an address for the domain.
3. The client sends packets toward that address. Routers forward them between networks.
4. For HTTPS, the client establishes a secure connection and checks the server's certificate for the domain.
5. The browser sends a request using the HTTP protocol, and the server returns a response with a status and, for a typical page request, its content.
6. The browser reads the HTML, requests other resources as needed, and renders the page for the user.

## 5. Difficulties faced

The evidence command first tried to store the HTTP code in `status`, a read-only zsh variable.

## 6. How I resolved them

Used `http_code` as the variable name and reran the HTTPS and DNS checks.

## 7. Evidence / files

[Selected connectivity and DNS output](network-output.txt). The listed addresses are the public site's IPv4 records.

## 8. Commit details

`Explain networking concepts and website communication`. [GitHub commit history](https://github.com/Illtrapx/digital-detective-8489/commits/main/).
