from flask import Flask, request, render_template_string

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Template for the home page
    template = """
    <h1>Bonjour, {{ name }}!</h1>
    <form method="GET">
        <input type="text" name="name" placeholder="Entrez votre nom" required>
        <input type="text" name="expression" placeholder="Entrez l'expression" required>
        <button type="submit">Valider</button>
    </form>
    <p>Résultat de l'expression : {{ result }}</p>
    """

    # Get the values of 'name' and 'expression' from the request parameters
    name = request.args.get('name', '')
    expression = request.args.get('expression', '')

    # Avoid executing dangerous commands
    if any(keyword in expression.lower() for keyword in [';', '&', '&&', '||', '`', '$(', 'eval']):
        result = "Invalid expression"
    else:
        try:
            # Render the provided 'expression' as a template string
            result = render_template_string(expression)
        except Exception as e:
            # Handle any errors that occur during the evaluation of the expression
            result = f"Erreur lors de l'évaluation de l'expression : {str(e)}"

    # Render the template with the provided 'name' and the evaluated 'result' of the expression
    return render_template_string(template, name=name, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

