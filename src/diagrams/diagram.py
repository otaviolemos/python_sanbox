from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom

with Diagram("Architecture with CDN and Cache", show=False):
    dns = Custom("", "./my_resources/dns.png")
    cdn = Custom("CDN", "./my_resources/cdn.png")
    lb = ELB("Load balancer")

    with Cluster("User"):
        user_group = [Custom("Web browser", "./my_resources/laptop.png"), 
            Custom("Mobile app", "./my_resources/mobile.png")]

    with Cluster("Web tier"):
        svc_group = [EC2("Server1"),
                     EC2("Server2")]

    with Cluster("Data tier"):
        master_db = RDS("Master DB")
        slave_db = RDS("Slave DB")
        master_db - [slave_db]

    redis = Custom("Redis cache", "./my_resources/redis.png")

    user_group >> lb >> svc_group
    user_group >> dns 
    user_group >> cdn
    svc_group >> master_db
    svc_group >> Edge(style="dashed") >> slave_db
    svc_group >> redis