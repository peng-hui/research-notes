#### Title: Awakening the Web’s Sleeper Agents: Misusing Service Workers for Privacy Leakage  
Service workers (SWs) in modern browsers provide web applications a set of features (e.g., pre-caching) that have enriched native applications.
Due to the problematic site isolation mechanisms, such SWs can be abused for history sniffing, i.e., inferring whether a victim has previously visited a particular website or not.

In this paper, the authors first conducted a large-scale measurement towards the usage of SWs in the wild.
They used Selenium to drive an instrumented Chromium browser to identify whether a website uses SWs and what particular functionalities are being used (if any).
The measurement demonstrates that 30,229 out of Alexa top 1M websites were using SWs.
Specifically, 8,559 websites use the caching functionality in their landing page.
Also, the usage of SWs grows progressively over time.

The authors find that when requesting the resource of the first party (e.g., example.com/img.jpg) by specifying the source URL of an iframe on a third-party website (e.g., website1.com), the request will go through the SWs of the first party.
The SW either directly fetches the requested resource from the network or from its SW cache if the website has been previously visited and the resource has been cached.
Therefore, the existence of the SW can imply the victim has visited the website, i.e., history sniffing.

The paper thus presents two attacks against SWs towards history sniffing -- (1) performance API-based attack and (2) timing-based attack.
The performance API-based attack utilizes the attributes of the APIs to identify if the SWs have been installed or not.
Timing-based attack, on the other hand, compares the difference of resource fetching time between SW cache and network.
Unlike browser cache, SW cache storage is persistent in nature unless it is explicitly removed.
Therefore, such attacks are more robust than existing browser cache-based ones.

The empirical study shows that Chromium-based browsers and Firefox are all vulnerable to such attacks, whereas Safari browsers are not because of their correct handling site isolation.
The authors also instrumented the Chromium browser for logging SW's FetchEvent listener into an automated resource profiling tool.
Among the 8,895 SWs with a FetchEvent listener on their landing pages,
the automated tool identified 6,706 websites that have resources suitable for the attacks.
Timing-based attack measures the time difference, and thus can potentially lead to false positives, i.e., an unsuccessful attack is labeled as a successful one.
Therefore, the authors manually evaluated the correctness of the reports and confirmed that the timing-based attack has only around a 1.5% false-positive rate.
The special ways that particular SWs handle fetch events and the use of content delivery networks are found to be the two reasons for the incorrect results.
In the last, the authors present several use cases towards registration inference, application-level inference, and fine-grained history sniffing, demonstrating the practicalness of the attacks.
In summary, the evaluation shows that a more strict site isolation mechanism is required to be equipped along with modern browsers.
