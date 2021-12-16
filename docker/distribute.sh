# Build N Run WEB Container
# 2021. 12. 14 Farrar142
##
docker_username="farrar142"
web_image_name="sampleproject_web"
web_container_name="web"
version="1"
port=8000 # Default django Port: 8000

echo "## Automation docker-web build and run ##"

# remove container
echo "=> Remove previous container..."
# cd docker/docker-dev
docker rm -f ${web_container_name}

# remove image
echo "=> Remove previous image..."
docker rmi -f ${docker_username}/${web_image_name}:${version}

# Run container
echo "=> Build new image..."
echo "=> Run container..."
docker-compose up -d
