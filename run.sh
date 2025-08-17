#!/bin/bash
# ASCII Shader Converter Launch Script
# Opens the tool in your default browser

echo "🎨 ASCII Shader Converter"
echo "=========================="
echo "Opening in your default browser..."
echo ""

# Try different methods to open the file
if command -v python3 &> /dev/null; then
    echo "Starting local server on http://localhost:8000"
    echo "Press Ctrl+C to stop the server"
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    echo "Starting local server on http://localhost:8000"
    echo "Press Ctrl+C to stop the server"
    python -m http.server 8000
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open index.html
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open index.html
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    # Windows
    start index.html
else
    echo "Please open index.html in your web browser manually"
fi
