#First Brigade Test Run
## Get Facts

##Summary
First test with Brigade.

This was my first use of Brigade.  I started out with the sample get facts run_brigade.py script from from [Patrick Ogenstad at Networklore].(https://networklore.com/introducing-brigade/)

The first_brigade.py script is my attempt to decompose the objects and resulting data structures.

My next Sunday afternoon project will involve generating configurations and applying them.

##Code Example

groups.yaml

        ---
        uwaco_network:
          brigade_username: cisco
          brigade_password: cisco
          brigade_nos: ios

hosts.yaml

        ---
        eu-med-as01:
          brigade_host: 10.1.10.25
          groups: ['uwaco_network']
      
        arctic-ds01-as01:
          brigade_host: 10.1.10.26
          groups: ['uwaco_network']

