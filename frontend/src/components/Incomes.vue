<template>
    <form>
        <div class="form-group">
            <label>От</label>
            <input type="text" class="form-control" placeholder="YYYY-MM-DD" v-model="date.from">
        </div>
        <div class="form-group">
            <label>До</label>
            <input type="text" class="form-control" placeholder="YYYY-MM-DD" v-model="date.to">
        </div>
        <div class="form-group">
            <label>Доход</label>
            <input type="text" disabled class="form-control" v-model="incomes">
        </div>
        <button class="btn btn-primary" @click="getIncomes(date)">Submit</button>
    </form>
</template>

<script>
    export default {
        data: () => ({
            date: {
                from: '',
                to: '',
            },
            incomes: 0
        }),
        methods: {
            getIncomes(date) {
                const self = this
                fetch('http://localhost:5000/incomes?from=' + date.from + '&to=' + date.to)
                    .then(resp => resp.json())
                    .then(data => {
                        self.incomes = (data[0].no_breakfast + data[0].with_breakfast) + ' ₽'
                    })
                    .catch(e => {
                        alert('OOPS!')
                    })
            }
        }
    }
</script>

<style scoped>

</style>