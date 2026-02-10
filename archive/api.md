restful api 

rest = representational state transfer 

6 principles: 
1. client-server: 
    client and server are in different processses and communicates via a transport that follows HTTP protocol over a TCP network 
2. **layered system**: 
    server must assume that the recipient of its info transportation can be an intermediate node & vice versa 
3. cache: 
    allow the server or an intermediate node to cache often made requests for optimisation purposes 
4. code on demand (opt): 
    API may include code 
5. **stateless**: 
    server can't save any info about the client n must include authentication requests in all APIs
6. uniform interface: 
    - unique identifier for each resource 
    - exchange resources btw cleint n server should be of the same format e.g. JSON
    - self descriptive messages on what each side wants 


resources: events & countries 


design process: what sort of things does front end want to ask of the backend 


e.g 

https://www.urbanoutfitters.com/womens-clothing?color=red,brown&price=50-100


https://www.depop.com/category/womens/tops/jumpers/?moduleOrigin=meganav&priceMin=10&priceMax=20&colours=white%2Cblack&isDiscounted=true

