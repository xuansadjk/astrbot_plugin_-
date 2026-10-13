from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from botpy.types.message import MarkdownPayload
from astrbot.api import logger

@register("ai_md_card", "YourName", "将AI回复自动转换为QQ官方Markdown卡片", "1.0.0")
class AiMdCardPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.on_llm_response()
    async def on_llm_response(self, event: AstrMessageEvent, response):
        ai_text = response.completion_text
        if not ai_text or ai_text.strip() == "":
            return

        # 构建Markdown内容
        markdown_content = f"# 🤖 AI 回复\n---\n{ai_text}"

        payload = MarkdownPayload(content=markdown_content)

        try:
            # 发送Markdown卡片
            await event.send(event.markdown_result(payload))
            # 阻止原本的纯文本消息再次发送，避免重复
            event.stop()
        except Exception as e:
            logger.error(f"发送Markdown卡片失败，将使用纯文本发送: {e}")
