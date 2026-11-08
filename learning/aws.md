# AWS Basics

## What is AWS?

Amazon Web Services (AWS) is a cloud platform that provides on-demand computing, storage, databases, networking, security, and other services. Instead of buying and maintaining physical servers, you can provision resources as needed and pay for what you use.

## Cloud service models

- **Infrastructure as a Service (IaaS):** You manage the operating system and application while AWS provides the underlying infrastructure. Amazon EC2 is a common example.
- **Platform as a Service (PaaS):** AWS manages more of the runtime and infrastructure so you can focus on deploying application code. AWS Elastic Beanstalk is one example.
- **Software as a Service (SaaS):** A complete application is delivered over the internet and managed by its provider. Amazon QuickSight is an AWS example.

These are useful general categories; AWS services can differ in how much management they take on.

## Global infrastructure

- **Region:** A geographic area where AWS has multiple data centers.
- **Availability Zone (AZ):** An isolated data center or group of data centers within a Region. Spreading an application across AZs can improve availability.
- **Edge location:** A site used by services such as Amazon CloudFront to deliver content closer to users.

Choose a Region based on latency, service availability, cost, and data residency requirements.

## Core services

| Area | Service | What it does |
|---|---|---|
| Compute | Amazon EC2 | Runs virtual machines that you manage |
| Compute | AWS Lambda | Runs code in response to events without managing servers |
| Containers | Amazon ECS / Amazon EKS | Runs and orchestrates containerized applications |
| Object storage | Amazon S3 | Stores objects such as files, backups, and static assets |
| Block storage | Amazon EBS | Provides disk volumes for EC2 instances |
| Relational database | Amazon RDS | Runs managed relational databases |
| NoSQL database | Amazon DynamoDB | Provides a managed key-value and document database |
| Networking | Amazon VPC | Creates an isolated network for AWS resources |
| Monitoring | Amazon CloudWatch | Collects metrics, logs, and alarms |

## Identity and security

- **AWS account:** The top-level boundary for resources, billing, and account settings.
- **AWS IAM:** Manages identities and permissions using users, roles, and policies.
- Give each identity only the permissions it needs (least privilege).
- Prefer temporary credentials and IAM roles over long-lived access keys.
- Enable multi-factor authentication (MFA), especially for privileged access.
- Use security groups as stateful traffic controls for network interfaces; allow only necessary inbound and outbound traffic.
- AWS secures the underlying cloud infrastructure; customers remain responsible for securing their data, identities, configurations, and workloads. The exact division depends on the service.

## Networking basics

- A **VPC** is a logically isolated network in an AWS Region.
- A **subnet** is a range of IP addresses in a VPC and belongs to one AZ.
- Public and private subnets are routing choices; a subnet is not public merely because of its name.
- Route tables control where network traffic is directed.
- An **Internet Gateway** enables internet connectivity for appropriately routed resources.
- A **NAT Gateway** lets resources in a private subnet initiate certain outbound internet connections without accepting unsolicited inbound connections.

## Storage and databases

- S3 stores objects in buckets and is commonly used for backups, data lakes, and static content. Choose access controls and lifecycle policies carefully.
- EBS provides persistent block storage typically attached to EC2 instances.
- RDS manages common relational database operations such as provisioning and backups; you still choose configurations and protect access.
- DynamoDB is a managed NoSQL database designed for key-value and document workloads.
- Select storage based on access patterns, durability, latency, consistency, and cost.

## Reliability, monitoring, and cost

- Use multiple AZs where availability requirements justify the added complexity and cost.
- Monitor application and infrastructure metrics and logs with CloudWatch; create alarms for important conditions.
- Tag resources to organize ownership, environment, and cost allocation.
- Review the AWS Pricing Calculator before deployment, set budgets and billing alerts, and remove unused resources.
- Understand that data transfer, storage, and requests can add costs beyond the main compute service.
- Back up important data and test restoration rather than assuming backups are usable.

## A safe beginner workflow

1. Secure the account: enable MFA, create least-privilege access, and avoid using root credentials for daily work.
2. Choose a Region and identify the services and data your application needs.
3. Design the network and access controls before exposing resources.
4. Estimate costs, set a budget alert, and add resource tags.
5. Deploy a small test workload, monitor it, and verify backups and access.
6. Delete test resources when finished and check the billing dashboard.

## Learn more

- [AWS Cloud Practitioner Essentials](https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Free Tier](https://aws.amazon.com/free/)
