// Template usada em https://next.json-generator.com para gerar 200 alunos. Foi necessário
// correr esta template 2 vezes devido a restrições do repeat().

[
    {
      'repeat(100)': {
        id: 'aluno_{{guid()}}',
        nome: '{{firstName()}}{{surname()}}',
        frequenta(tags) {
          const fruits = [':PRC2021', ':DC2021', ':IS2021', ':SPLN2021'];
          let fruit = tags.integer(0, fruits.length - 1);
          let fruit2 = tags.integer(0, fruits.length - 1);
          
          if(fruit != fruit2){
              return [fruits[fruit], fruits[fruit2]];
          } else {
              return [fruits[fruit]];
          }
          
          
        }
      }
    }
  ]

