### Title: Automatic Policy Generation for Inter-Service Access Control of Microservices

Cloud applications are usually composed of multiple microservices each response for different business functions.
Microservices' code usually contains unpatched vulnerabilities which can be exploited by attackers to compromise the microservers and further the whole application.
Enforcing inter-service access control policies is useful to guarantee the integrity of the application and reduce the possibility of compromised services from attacking other services.
Some existing tools rely on experts to specify the inter-service access control policies; 
other automated tools cannot achieve high accuracy.

This paper proposes an automated inter-service access control policy mechanism --- AutoArmor.
AutoArmor marks the HTTP request APIs as sinks and performs an inter-procedural backward data flow analysis.
The data flow analysis is standard and can construct slices for the relevant arguments like URLs used in the APIs.
With the slices, 
AutoArmor outputs a manifest file describing the requests that a microservice might initiate.
AutoArmor employs a permission graph to better present the potentially diverse versions of the same services. 
It translates each request edge in the permission graph into an access control policy.
The permission graph merges the same policies across different versions to accelerate the policy update and removal.
AutoArmor is implemented for analyzing microservices written in diverse programming languages, such as Java, Ruby, etc., using over 16K LoC.

AutoArmor was evaluated on five popular open-source microservice applications.
AutoArmor achieved 100% accuracy in request identification, a 100% extraction rate for the method and port attributes, and a 99.5% extraction rate for URL attribute.
With respect to the security property, the evaluation shows AutoArmor could successfully prevent all three types of inter-service attacks.
AutoArmor is also effective, scalable, and with low end-to-end latency.
However, AutoArmor has both FPs and FNs.
The FPs are because the static analysis is not able to identify unnecessary code,
while the FNs are caused by the inaccuracy in the data flow analysis, e.g., complicated attribute data flow, 
These two limitations cannot be solved by the nature of current static analysis based method.
