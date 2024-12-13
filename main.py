import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

class abcHandler(webapp2.RequestHandler):
    def get(self):
        colorful_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Colorful Response</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    background-color: #f0f8ff;
                    color: #2c3e50;
                }
                h1 {
                    font-size: 48px;
                    color: #e74c3c;
                    text-shadow: 2px 2px 4px #000000;
                }
                p {
                    font-size: 24px;
                    color: #3498db;
                }
            </style>
        </head>
        <body>
            <h1>Welcome!</h1>
            <p>abc!</p>
        </body>
        </html>
        """
        self.response.write(colorful_html)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Home Page!')

class CalculatorHandler(webapp2.RequestHandler):
    def get(self):
        calculator_html = """
       <!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .btn {
            padding: 15px;
            font-size: 18px;
            font-weight: bold;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s ease;
        }

        .btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white shadow-lg rounded-lg p-6 w-96">
        <h1 class="text-2xl font-bold text-center text-gray-700 mb-4">Calculator</h1>
        <div class="flex flex-col items-center">
            <input
                type="text"
                id="display"
                readonly
                class="w-full mb-4 p-3 text-right border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="0"
            >
            <div class="flex">
                <!-- Number buttons on the left -->
                <div class="grid grid-cols-3 gap-2 w-3/4">
                    <button class="btn" onclick="addToDisplay('1')">1</button>
                    <button class="btn" onclick="addToDisplay('2')">2</button>
                    <button class="btn" onclick="addToDisplay('3')">3</button>
                    <button class="btn" onclick="addToDisplay('4')">4</button>
                    <button class="btn" onclick="addToDisplay('5')">5</button>
                    <button class="btn" onclick="addToDisplay('6')">6</button>
                    <button class="btn" onclick="addToDisplay('7')">7</button>
                    <button class="btn" onclick="addToDisplay('8')">8</button>
                    <button class="btn" onclick="addToDisplay('9')">9</button>
                    <button class="btn" onclick="clearDisplay()">C</button>
                    <button class="btn" onclick="addToDisplay('0')">0</button>
                    <button class="btn" onclick="calculate()">=</button>
                </div>
                <!-- Operation buttons on the right -->
                <div class="flex flex-col gap-2 w-1/4 ml-2">
                    <button class="btn" onclick="addToDisplay('+')">+</button>
                    <button class="btn" onclick="addToDisplay('-')">-</button>
                    <button class="btn" onclick="addToDisplay('*')">*</button>
                    <button class="btn" onclick="addToDisplay('/')">/</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        function addToDisplay(value) {
            document.getElementById('display').value += value;
        }
        function clearDisplay() {
            document.getElementById('display').value = '';
        }
        function calculate() {
            try {
                let result = eval(document.getElementById('display').value);
                document.getElementById('display').value = result;
            } catch (error) {
                document.getElementById('display').value = 'Error';
            }
        }
    </script>
</body>
</html>

        """
        self.response.write(calculator_html)

# Combine all routes into a single WSGIApplication
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/abc', abcHandler),
    ('/home', HomeHandler),
    ('/calculator', CalculatorHandler),
], debug=True)