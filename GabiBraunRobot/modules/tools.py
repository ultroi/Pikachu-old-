

__help__ = "Tools"
• Snipe 
──「 Sudo only: 」──
-> /snipe <chatid> <string>
Make me send a message to a specific chat.

• Translator
• /tr or /tl (language code) as reply to a long message
Example: 
  /tr en: translates something to english
  /tr hi-en: translates hindi to english

• Telegraph
 - /tm: Get Telegraph Link of Replied Media
 - /txt: Get Telegraph Link of Replied Text

• Time
 • /time <query>: Gives information about a timezone.
Available queries: Country Code/Country Name/Timezone Name
• [🕐 Timezones list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

• Sed\regex
 • s/<text1>/<text2>(/<flag>): Reply to a message with this to perform a sed operation on that message, replacing all occurrences of 'text1' with 'text2'. Flags are optional, and currently include 'i' for ignore case, 'g' for global, or nothing. Delimiters include /, _, |, and :. Text grouping is supported. The resulting message cannot be larger than 4096.
Reminder: Sed uses some special characters to make matching easier, such as these: +*.?\
If you want to use these characters, make sure you escape them!
Example: \?.

Report bugs - @PikachuHelpSupport
"""
__mod_name__ = "Tools"

