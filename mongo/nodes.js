conn = new Mongo();
db = conn.getDB("puppet");
db["nodes"].insert(
  {
    node: "agent.billcloud.local",
    classes: ['common', 'puppet', 'dns', 'ntp']
  }
)
