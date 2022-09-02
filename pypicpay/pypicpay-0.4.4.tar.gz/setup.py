# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypicpay']

package_data = \
{'': ['*']}

install_requires = \
['requests']

setup_kwargs = {
    'name': 'pypicpay',
    'version': '0.4.4',
    'description': 'Aceite PicPay e faça parte do movimento que está revolucionando a relação com o dinheiro no Brasil.',
    'long_description': '# Pypicpay\n\nAceite PicPay e faça parte do movimento que está revolucionando a relação com o dinheiro no Brasil.\n\n![Python package](https://github.com/hudsonbrendon/picpay-python/workflows/Python%20package/badge.svg?branch=master)\n[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/picpay-python.svg?style=flat)](https://github.com/hudsonbrendon/picpay-python/issues?sort=updated&state=open)\n![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)\n\n![PicPay](https://logodownload.org/wp-content/uploads/2018/05/picpay-logo-1.png)\n\n# Recursos Disponíveis\n\n- [x]  Requisição de Pagamento\n- [x]  Cancelamento\n- [x]  Status\n- [x]  Notificação\n\n# Instalação\n\n```bash\n$ pip install pypicpay\n```\n# Modo de usar\n\nTodas as APIs do PicPay Developers foram desenvolvidas baseadas na tecnologia REST, seguindo os atuais padrões técnicos de mercado. Tudo isso para que a experiência na hora da integração seja a mais fácil possível. Todas as URLs são amigáveis e orientadas a recursos e utilizam os padrões do protocolo HTTP como autenticação, verbos e códigos de retorno. Isso permite que APIs possam ser utilizadas por clientes HTTP já existentes. Todas as respostas são retornadas no formato JSON.\n\nComo pode ser visto abaixo, as APIs foram cuidadosamente trabalhadas para que os termos de negócios contidos sejam facilmente entendidos por desenvolvedores que não tenham conhecimento prévio do sistema. Elas foram meticulosamente estudadas para que um nome de campo em um endpoint tenha rigorosamente o mesmo significado em outros recursos.\n\nAtenção: Todos os testes devem ser realizados em produção sem ônus ao desenvolvedor: todos os pagamentos realizados podem ser imediatamente estornados (tanto pela API quanto pelo painel do lojista).\n\nSaiba mais em: https://ecommerce.picpay.com/doc/#tag/Introducao\n\n## Requisição de Pagamento\n\nSeu e-commerce irá solicitar o pagamento de um pedido através do PicPay na finalização do carrinho de compras. Após a requisição http, o cliente deverá ser redirecionado para o endereço informada no campo paymentUrl para que o mesmo possa finalizar o pagamento.\n\nAssim que o pagamento for concluído o cliente será redirecionado para o endereço informada no campo returnUrl do json enviado pelo seu e-commerce no momento da requisição. Se não informado, nada acontecerá (o cliente permanecerá em nossa página de checkout).\n\nCaso seja identificado que seu cliente também é cliente PicPay, iremos enviar um push notification e uma notificação dentro do aplicativo PicPay avisando sobre o pagamento pendente. Para todos os casos iremos enviar um e-mail de pagamento pendente contendo o link de nossa página de checkout.\n\nSaiba mais em: https://ecommerce.picpay.com/doc/#tag/Requisicao-de-Pagamento\n\n```python\nfrom pypicpay import PicPay\n\npicpay = PicPay(\n    x_picpay_token="X_PICPAY_TOKEN", x_seller_token="X_SELLER_TOKEN"\n)\n\npayment = picpay.payment(\n    reference_id=102030,\n    callback_url="https://picpay.com/site",\n    return_url="http://www.sualoja.com.br/cliente/pedido/102030",\n    value=20.50,\n    expires_at="2022-05-01T16:00:00-03:00",\n    buyer={\n        "firstName": "João",\n        "lastName": "Da Silva",\n        "document": "123.456.789-10",\n        "email": "teste@picpay.com",\n        "phone": "+55 27 12345-6789",\n    },\n)\n```\n\n## Cancelamento\n\nUtilize este método para solicitar o cancelamento/estorno de um pedido. Valem as seguintes regras:\n\na) Se já foi pago, o cliente PicPay será estornado caso sua conta de Lojista no PicPay tenha saldo para realizar o estorno e caso o cliente PicPay tenha recebido algum cashback nesta transação, este valor será estornado do cliente (para isto o mesmo deve possuir saldo). Todas esses requisitos devem ser cumpridos para que o estorno da transação ocorra com sucesso.\n\nb) Se ainda não foi pago, a transação será cancelada em nosso servidor e não permitirá pagamento por parte do cliente PicPay;\n\nSaiba mais em: https://ecommerce.picpay.com/doc/#tag/Cancelamento\n\n```python\nfrom pypicpay import PicPay\n\n\npicpay = PicPay(\n    x_picpay_token="X_PICPAY_TOKEN", x_seller_token="X_SELLER_TOKEN"\n)\n\ncancellation = picpay.cancellation(reference_id=102030)\n```\n\n## Status\n\nUtilize este método para solicitar o status de um pedido.\n\nSaiba mais em: https://ecommerce.picpay.com/doc/#operation/getStatus\n\n```python\nfrom pypicpay import PicPay\n\n\npicpay = PicPay(\n    x_picpay_token="X_PICPAY_TOKEN", x_seller_token="X_SELLER_TOKEN"\n)\n\nstatus = picpay.status(reference_id=102030)\n```\n\n## Notificação\n\nIremos enviar uma notificação para sua loja nas seguintes trocas de status:\n\n- Pedido expirado: não é mais possível paga-lo usando PicPay;\n- Pagamento em análise: usuário pagou porém o pagamento está sob análise;\n- Pedido pago;\n- Pedido completado: saldo disponível para saque;\n- Pagamento devolvido: foi pago e estornado para o cliente;\n- Pagamento com chargeback: cliente solicitou à operadora o cancelamento do pagamento;\n\nSaiba mais em: https://ecommerce.picpay.com/doc/#tag/Notificacao\n\n```python\nfrom pypicpay import PicPay\n\n\npicpay = PicPay(\n    x_picpay_token="X_PICPAY_TOKEN", x_seller_token="X_SELLER_TOKEN"\n)\n\nnotification = picpay.notification(reference_id=3434)\n```\n\n# Contribua\n\nClone o projeto repositório:\n\n```bash\n$ git clone https://github.com/hudsonbrendon/pypicpay.git\n```\n\nCertifique-se de que o [Poetry](https://python-poetry.org/) está instalado, caso contrário:\n\n```bash\n$ pip install -U poetry\n```\n\nInstale as dependências:\n\n```bash\n$ poetry install\n```\nPara executar os testes:\n\n```bash\n$ pytest\n```\n\n# Dependências\n\n- [Python >=3.8](https://www.python.org/downloads/release/python-388/)\n\n# Licença\n\n[MIT](http://en.wikipedia.org/wiki/MIT_License)\n\n',
    'author': 'Hudson Brendon',
    'author_email': 'contato.hudsonbrendon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hudsonbrendon/picpay#readme',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
