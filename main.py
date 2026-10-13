from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from botpy.types.message import MarkdownPayload

@register("md_card", "我", "AI转卡片", "1.0.0")
class MdCard(Star):
    @filter.on_llm_response()
    async def on_resp(self, event: AstrMessageEvent, response):
        text = response.completion_text
        if not text: return
        payload = MarkdownPayload(content=f"# AI 回复\n\n{text}")
        await event.send(event.markdown_result(payload))
