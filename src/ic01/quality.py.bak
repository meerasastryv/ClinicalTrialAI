AMBIGUOUS_WORDS = [
   "easy",
   "quick",
   "quickly",
   "fast",
   "efficient",
   "simple",
   "robust",
   "flexible",
   "appropriate",
   "user-friendly",
   "seamless"
]


def analyze_requirement(req):

   text = req.text.lower()

   ambiguous_words_found = []

   for word in AMBIGUOUS_WORDS:
       if word in text:
           ambiguous_words_found.append(word)

   score = 100

   score -= len(ambiguous_words_found) * 20

   if score < 0:
       score = 0

   return {
       "id": req.id,
       "score": score,
       "ambiguous_words": ambiguous_words_found,
       "testable": len(ambiguous_words_found) == 0
   }

