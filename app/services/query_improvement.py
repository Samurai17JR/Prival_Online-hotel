from textblob import TextBlob

class QueryImprovementService:
    @classmethod
    def improve_query(cls, query: str) -> str:
        # Исправление опечаток
        blob = TextBlob(query)
        corrected = str(blob.correct())

        # Добавление синонимов для ключевых слов
        synonyms = {
            "отель": ["гостиница", "хостел"],
            "номер": ["комната", "апартаменты"],
            "бронирование": ["резервирование", "заказ"],
            "цена": ["стоимость", "тариф"],
        }

        improved = corrected
        for word, syns in synonyms.items():
            if word in improved.lower():
                # Добавить синонимы в запрос для лучшего поиска
                improved += f" {' '.join(syns)}"

        return improved