### Title: Do Cookie Banners Respect my Choice? Measuring Legal Compliance of Banners from IAB Europe’s Transparency and Consent Framework (S&P'20)
Cookie banners are commonly used by many websites in Europe after the
General Data Protection Regulation (GDPR) and ePrivacy Directive (ePD),
especially for today\'s advertisement business. This paper
systematically studies the inconsistency between the user interface (UI)
choices and the real behaviors behind the cookie banners. The paper
first introduces IAB Europe\'s Transparency and Consent Framework (TCF)
and its Consent Management Providers (CMPs), in particular, the consent
string contains at least three attributes: 1) \"cmpId\" to identify the
responsible CMP, 2) \"allowedPurposeIds\" to denote the purposes of data
processing, and 3) \"allowedVendorIds\" for the advertisers. The consent
is then stored in the browser, and the third parties, e.g., advertisers,
can query it through four methods: 1) standard APIs, such as javascript
function \"\_\_cmp()\" and iframe \"\_\_cmpLocator\", can be directly or
indirectly called, 2) shared cookie, 3) URL-based methods like GET
parameters and HTTP redirecting mechanisms, and 4) non-standard
SafeFrames by calling \"\_\_cmp()\". With a thorough legal analysis of
the GDPR and ePD, the authors propose four potential legal violations: 1) consent stored before choice, 2) no way to opt out, 3) pre-selected
choices and 4) no-respect of choice. The authors design and implement a
Selenium-instrumented Chromium tool, Cookinspect, to detect whether a
website enables a TCF cookie banner by checking whether \"\_\_cmp()
function is defined. Besides, Cookinspect can intercept the consent
string by inserting consent queries as an advertiser and monitoring the
network traffic. A website violates 1) consent stored before choice if
there exist accepted purposes even if no user action is performed, 2) no
way to opt out if nowhere can refuse the consent, 3) pre-selected
choices if there is at least one pre-selected checkbox for at least one
purpose, and 4) non-respect of choice if user choices do not really
behave in the browser, e.g., refusal of the consent. The latter four
violations are examined through manually checking (semi-automatic
crawl), while the first is fully automatic (automatic crawl). The
authors apply Cookieinspect on 22,949 websites and detect 1,426 websites
with cookie banners, and 141 (10%) out of 1,426 websites violate the
consent store before choice; A more precise analysis on a subset of 560
websites finds that 236 (47%) nudge the users towards accepting the
pre-selected choices, and 38 (7%) do not allow refusing the consent. In
summary, at least one suspected violation exists in 304 (54%) out of 560
websites. The paper also analyzes the prevalence of the TCF banners
based on the domains, CMPs, etc. At last, a browser extension, named
Cookie Glasses, is published to allow end-users to check their consent
stored by the CMPs.
