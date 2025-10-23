# WAHA-Messaging-Tool

- Install WAHA docker image:
```
# Login to Docker
docker login -u devlikeapro -p {KEY}

# Pull the WAHA Plus image
docker pull devlikeapro/waha-plus

# Logout from Docker
docker logout
```

- Run the docker image using the following command
```
docker run -it -p 3000:3000 devlikeapro/waha-plus
```

- Dahboard can be accessed through this endpoint
```
https://localhost:3000/dashboard
```

  
