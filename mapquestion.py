# -*- coding: utf-8 -*-

from ollama import ChatResponse
from ollama import chat

who_where_what = [
    {
        "who": "大学生",
        "where": "ニューヨーク",
        "what": "旅行"
    },
    {
        "who": "長時間歩けない60代後半母と40代の娘",
        "where": "ロンドン",
        "what": "旅行"
    },
    {
        "who": "会社員",
        "where": "サンフランシスコ",
        "what": "学会出張"
    },
    {
        "who": "会社員",
        "where": "ラスベガス",
        "what": "カンファレンス出張"
    },
    {
        "who": "大学生",
        "where": "ヨーロッパ",
        "what": "バックパッキング"
    },
    {
        "who": "新婚夫婦",
        "where": "パリ",
        "what": "ハネムーン"
    },
    {
        "who": "20代学生",
        "where": "シドニー",
        "what": "短期留学"
    },
    {
        "who": "30代アート好きカップル",
        "where": "フィレンツェ",
        "what": "美術館巡り"
    },
    {
        "who": "20代男性",
        "where": "ハワイ",
        "what": "サーフィン"
    },
    {
        "who": "大学生2人組",
        "where": "北海道",
        "what": "スノボ"
    }
]

# where_who_whatの情報をもとに、scenarios = role, situation, instructionを生成
scenarios = []


def generate_situation(who, where, what):
    role = f"あなたは{who}です。{where}へ{what}に行くことになりました。"
    prompt = f"{who}として、気になる質問を列挙してください。"
    format = f"質問は一文で背景や意図が伝わるようにしてください。Markdownの簡潔なリスト形式で質問のみを出力してください。"
    prompt_text = (
        f"Role: {role}\n"
        f"Prompt: {prompt}\n"
        f"Format: {format}\n"
        "------------------------\n"
    )
    res: ChatResponse = chat(
        model='phi4:14b',
        messages=[
            {
                'role': 'user',
                'content': prompt_text,
            },
        ],
    )
    return res.message.content


def generate_prompts_with_ollama(scenarios):
    for www in who_where_what:
        print(f"www: {www['who']} {www['where']} {www['what']}")
        situation = generate_situation(www["who"], www["where"], www["what"])
        print(situation)


if __name__ == "__main__":
    generate_prompts_with_ollama(scenarios)
