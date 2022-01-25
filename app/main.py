import os
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from discord_webhook import DiscordWebhook, DiscordEmbed

if 'WEBHOOK_URL' in os.environ:
    WEBHOOK_URL = os.environ['WEBHOOK_URL']
else:
    exit("No Webhook defined! Please set WEBHOOK_URL");


app = FastAPI()


class SQProject(BaseModel):
    key: str
    name: str
    url: str

class SQCondition(BaseModel):
    errorThreshold: str
    metric: str
    onLeakPeriod: bool
    operator: str
    status: str
    value: Optional[str]

class SQQualityGate(BaseModel):
    conditions: List[SQCondition]
    name: str
    status: str

class SonarQubeEvent(BaseModel):
    serverUrl: str
    taskId: str
    status: str
    analysedAt: str
    project: SQProject
    properties: Optional[dict]
    qualityGate: SQQualityGate

@app.post("/")
def recieve_webhook(event: SonarQubeEvent):
    webhook = DiscordWebhook(url=WEBHOOK_URL)
    embed = DiscordEmbed(title=event.project.name, url=event.project.url, description=event.status, color=('013220' if event.status == 'SUCCESS' else 'FF0000'))
    for condition in event.qualityGate.conditions:
        metric = condition.metric.replace("_", " ").replace("new", "").title()
        embed.add_embed_field(name=f"{metric}", value=condition.status)
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    return True