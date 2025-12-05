// Initialize MongoDB database for Chrome Extensions

db = db.getSiblingDB('chrome_extensions');

// Create collection if it doesn't exist
db.createCollection('extensions');

// Create indexes for efficient queries
db.extensions.createIndex({ extension_id: 1 }, { unique: true });
db.extensions.createIndex({ title: "text", full_description: "text" });
db.extensions.createIndex({ "jtbd": 1 });
db.extensions.createIndex({ "metadata.imported_at": -1 });

print('Database initialized successfully');
print('Database: chrome_extensions');
print('Collection: extensions');
print('Indexes created for: extension_id, full-text search, jtbd, imported_at');
