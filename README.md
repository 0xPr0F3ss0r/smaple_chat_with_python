# 🔌 Python Socket Chat Application  
*A real-time terminal-based chat system using Python sockets and threading.*  

## Key Features
- Real-time messaging between clients  
- Multi-threaded server handles multiple connections  
- Custom commands: `exit`, `clear`/`cls`, `color [x]`  
- Automatic disconnect detection  
## Tech Stack
- `socket` · `threading` · `os` (Pure Python - no dependencies)  
## Quick Start (Code Blocks)
1. **Run the server**:  
   ```bash 
   python server.py
   Listens on 0.0.0.0:7777
   python client.py
   Connects to your local IP
## Commands (Table)
| Command       | Action                  |
|---------------|-------------------------|
| `exit`        | Quit the chat           |
| `clear`/`cls` | Clean the terminal      |
| `color [x]`   | Change text color (Windows) |
## Project Files (Code Block)
your-project/
├── server.py    # Handles connections/messages
├── client.py    # Sends/receives messages
└── README.md    # This file
## License

[MIT](https://choosealicense.com/licenses/mit/) . By kebir Hani