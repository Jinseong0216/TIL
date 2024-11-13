import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000,
    },
    {
      name: '김두리',
      balance: 10000,
    },
    {
      name: '김서이',
      balance: 100,
    },
  ])

  // 특정 이름과 일치하는 사용자 정보를 반환하는 getter
  const getBalanceByName = computed(() => {
    return (name) => {
      return balances.value.find((user) => user.name === name) || null
    }
  })

  const increamentBalance = function (name) {
    const balance = getBalanceByName.value(name)
    balance.balance += 1000
  }

  return { balances, getBalanceByName, increamentBalance }
})
