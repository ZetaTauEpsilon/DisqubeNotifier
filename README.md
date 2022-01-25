<h1 align="center">DisqubeNotifier</h1>

&nbsp;&nbsp;&nbsp;DisqubeNotifier is a lightweight FastAPI implementation of a Webhook bridge between SonarQube and Discord. Simply run DisqubeNotifier with a webhook URL pointing to your channel of choice and direct SonarQube to DisqubeNotifier's URL and *viola!*

**Codesnap Placeholder**<br>
**Sample Embed Placeholder**

# Quickstart

**Create a Discord Integration:**<br>
Edit Channel -> Integrations -> Create Webhook
- Set Avatar and "Name" for the Webhook notifications to use.
- **Copy Webhook Url** - This is what you will need when running your DiscqubeNotifier container.

**Run the container:**

```
docker run -d -p 42000:42000 -e WEBHOOK_URL=[YOUR WEBHOOK URL HERE] zetatauepsilon/disqubenotifier:latest
```

**Configure SonarQube:** <br>
Administration -> Configuration -> Webhooks -> Create
- Set name to DisqubeNotifier
- Input URL where SonarQube can access DisqubeNotifier (If on the same machine, this may be http://localhost:42000)

All Done!
