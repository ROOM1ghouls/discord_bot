import discord

_webhook_cache: dict[int, discord.Webhook] = {}

async def send_as_user(channel: discord.TextChannel, user: discord.User | discord.Member, content: str,override_name: str = None)-> discord.Message:
    if channel.id not in _webhook_cache:
        webhooks = await channel.webhooks()
        hook = discord.utils.get(webhooks, name="FilterBotWebhook")

        if not hook:
            hook = await channel.create_webhook(name="FilterBotWebhook")

        _webhook_cache[channel.id] = hook

    webhook = _webhook_cache[channel.id]

    return await webhook.send(  # 반드시 return!
        content,
        username=override_name,
        avatar_url=user.display_avatar.url,
        allowed_mentions=discord.AllowedMentions.none(),
        wait=True
    )
