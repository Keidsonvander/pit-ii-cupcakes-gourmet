const carrinho = new Map();
const qtdCarrinho = document.getElementById('qtdCarrinho');
const resumoPedido = document.getElementById('resumoPedido');
const mensagem = document.getElementById('mensagem');

function atualizarResumo(){
  let totalItens = 0;
  let total = 0;
  const linhas = [];
  carrinho.forEach(item => {
    totalItens += item.quantidade;
    total += item.preco * item.quantidade;
    linhas.push(`<div class="item-resumo"><span>${item.nome} x${item.quantidade}</span><strong>R$ ${(item.preco*item.quantidade).toFixed(2).replace('.', ',')}</strong></div>`);
  });
  qtdCarrinho.textContent = totalItens;
  resumoPedido.className = carrinho.size ? 'resumo' : 'resumo-vazio';
  resumoPedido.innerHTML = carrinho.size ? `${linhas.join('')}<hr><div class="item-resumo"><strong>Total</strong><strong>R$ ${total.toFixed(2).replace('.', ',')}</strong></div>` : 'Adicione produtos ao carrinho.';
}

document.querySelectorAll('.adicionar').forEach(botao => {
  botao.addEventListener('click', () => {
    const id = Number(botao.dataset.id);
    const atual = carrinho.get(id) || {id, nome: botao.dataset.nome, preco: Number(botao.dataset.preco), quantidade: 0};
    atual.quantidade += 1;
    carrinho.set(id, atual);
    atualizarResumo();
    mensagem.textContent = `${atual.nome} adicionado ao carrinho.`;
  });
});

document.getElementById('abrirCarrinho').addEventListener('click', () => {
  document.getElementById('pedido').scrollIntoView({behavior:'smooth'});
});

document.getElementById('formPedido').addEventListener('submit', async (event) => {
  event.preventDefault();
  mensagem.textContent = '';
  if (!carrinho.size){
    mensagem.textContent = 'Adicione pelo menos um cupcake ao carrinho.';
    return;
  }

  const payload = {
    cliente: document.getElementById('cliente').value.trim(),
    telefone: document.getElementById('telefone').value.trim(),
    endereco: document.getElementById('endereco').value.trim(),
    itens: [...carrinho.values()].map(({id, quantidade}) => ({id, quantidade}))
  };

  try {
    const resposta = await fetch('/api/pedidos', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify(payload)
    });
    const dados = await resposta.json();
    if (!resposta.ok) throw new Error(dados.mensagem || 'Não foi possível concluir o pedido.');
    mensagem.textContent = `${dados.mensagem} Número: ${dados.pedido_id}. Total: R$ ${dados.total.toFixed(2).replace('.', ',')}`;
    carrinho.clear();
    atualizarResumo();
    event.target.reset();
  } catch (erro) {
    mensagem.textContent = erro.message;
  }
});

atualizarResumo();
