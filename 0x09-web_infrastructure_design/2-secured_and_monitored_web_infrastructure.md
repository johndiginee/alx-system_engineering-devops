For every additional element, why you are adding it
It is usually one of the first things people look at to get to know a brand and therefore helps form the first impression. 

What are firewalls for
A firewall is a division between a private network and an outer network, often the internet, that manages traffic passing between the two networks. It’s implemented through either hardware or software. Firewalls are both networking and security technology.

Why is the traffic served over HTTPS
HTTPS uses the SSL/TLS protocol to encrypt communications so that attackers can't steal data. SSL/TLS also confirms that a website server is who it says it is, preventing impersonations.

What monitoring is used for
Also known as availability monitoring, uptime monitoring assesses the website, servers, or applications for availability and accessibility. It's an evaluation approach to monitor a website or web application to test its availability from different locations across the world.

How the monitoring tool is collecting data
Website monitoring is a comprehensive approach to monitor a website or web service by tracking critical performance indicators using a set of tools and best practices to ensure consistent availability and seamless user experience even during unexpected traffic spikes.

Explain what to do if you want to monitor your web server QPS
qps is a monitor that displays the status of the processes currently in existence, much like top(1) or ps(1). The user interface uses the Qt toolkit, and most operations should be fairly intuitive.

Why terminating SSL at the load balancer level is an issue
However, such practice implies that SSL termination at the Load Balancer also poses a security risk because the data that are passing across the network from the load balancer to the App Server are now unencrypted, and that will leave applications vulnerable to Man-in-the-Middle Attack (MITM)

Why having only one MySQL server capable of accepting writes is an issue
The MySQL master-master replication user may lose certain transactions if one or more master nodes fail as a result of the asynchronous replication amongst all master nodes. The user cannot be certain that backups created on each master node have the same data due to asynchronous replication.

Why having servers with all the same components (database, web server and application server) might be a problem
With the db and app hosted on the same machine, you can forbid any external access to the database and as such, only having credentials of the database does not grant you any access, you will need server access for that
