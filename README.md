# highload-homework-13

### Handmade CDN

Your goal is to create your own cdn for delivering millions of images across the globe.  
- Set up 5 containers - bind server, load balancer, node1, node2, node3.
- Try to implement different balancing approaches. 
- Implement efficient caching 

# Installing

```
git clone https://github.com/god-of-north/highload-homework-13.git
cd highload-homework-13
docker-compose build
docker network create --gateway 172.16.1.1 --subnet 172.16.1.0/24 hw13_subnet
```

# Environment

![docker compose network diagram](/assets/diagram.png)


# Testing CDN
```
>docker exec -it highload-homework-13_tester_1 ping cdn.picture.com

PING cdn.picture.com (172.16.1.30) 56(84) bytes of data.
64 bytes from highload-homework-13_load_balancer_world_1.hw13_subnet (172.16.1.30): icmp_seq=1 ttl=64 time=0.351 ms
```

# Testing Load Balancers
```
docker-compose run --rm siege -c25 -t10s -b "http://cdn.picture.com/1.jpg"
```
