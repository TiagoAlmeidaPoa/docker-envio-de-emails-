from bottle import route, run, request

@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    return 'Mensagem enfileirada ! Assunto: {} Mensagem: {}'.format(
        assunto, mensagem 
    )

if _name_=='_main_':
    run(host='0.0.0.0', port=8080, debug=True)