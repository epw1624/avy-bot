# avy-bot
Discord bot that provides avalanche forecasts from the Avalanche Canada API

### Bot Commands <br>
All bot commands are prefixed with **!avy-bot**<br>

**!avy-bot forecast \[latitude\] \[longitude\]**<br>
Gets an avalanche forecast for the location described by the latitude and longitude provided<br>

**!avy-bot set_home \[latitude\] \[longitude\]**<br>
Sets the home zone of the bot to be the location described by the provided latitude and longitude<br>
This allows users to get forecasts for this region without specifying coordinates<br>

**!avy-bot home**<br>
Gets and avalanche forecast for the bot's home zone<br>
The home zone must first be set using the **!avy-bot set_home** command<br>
