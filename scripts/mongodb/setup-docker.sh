#!/bin/bash
# MongoDB Docker Setup для Chrome Extensions
# Usage: ./setup-docker.sh

cd "$(dirname "$0")"

echo "🚀 Starting MongoDB Docker container..."

# Stop existing container if any
docker-compose down 2>/dev/null || true

# Start MongoDB
docker-compose up -d

# Wait for MongoDB to be ready
echo "⏳ Waiting for MongoDB to start..."
sleep 5

# Test connection
if docker exec extensions-mongodb mongosh \
  -u admin -p simple123 \
  --eval "db.adminCommand('ping')" \
  2>/dev/null | grep -q "ok"; then
  echo "✅ MongoDB is ready!"
else
  echo "⏳ MongoDB still starting, waiting more..."
  sleep 5
  if docker exec extensions-mongodb mongosh \
    -u admin -p simple123 \
    --eval "db.adminCommand('ping')" \
    2>/dev/null | grep -q "ok"; then
    echo "✅ MongoDB is ready!"
  else
    echo "❌ MongoDB failed to start"
    exit 1
  fi
fi

echo ""
echo "📊 Connection details:"
echo "  URI: mongodb://admin:simple123@localhost:27017"
echo "  Database: chrome_extensions"
echo "  Collection: extensions"
echo ""
echo "✅ MongoDB is ready for use!"
