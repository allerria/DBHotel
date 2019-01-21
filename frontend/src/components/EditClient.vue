<template>
    <form>
        <div class="form-group">
            <label>Id</label>
            <input type="number" disabled class="form-control" v-model="client.id">
        </div>
        <div class="form-group">
            <label>Имя</label>
            <input type="text" class="form-control" v-model="client.first_name">
        </div>
        <div class="form-group">
            <label>Фамилия</label>
            <input type="text" class="form-control" v-model="client.last_name">
        </div>
        <div class="form-group">
            <label>Номер</label>
            <input type="number" class="form-control" v-model="client.room_number">
        </div>
        <div class="form-group">
            <label>Дата прибытия</label>
            <input type="text" placeholder="YYYY-MM-DD" class="form-control" v-model="client.arrival">
        </div>
        <div class="form-group">
            <label>Дата отправления</label>
            <input type="text" placeholder="YYYY-MM-DD" class="form-control" v-model="client.departure">
        </div>
        <div class="form-group">
            <label>Оплачено</label>
            <input type="checkbox" v-model="client.is_paid">
        </div>
        <div class="form-group">
            <label>С завтраком</label>
            <input type="checkbox" v-model="client.with_breakfast">
        </div>
        <button class="btn btn-primary" @click="editClient(client)">Submit</button>
    </form>
</template>

<script>
    export default {
        data: () => ({
            client: {
                id: '',
                first_name: '',
                last_name: '',
                room_number: '',
                arrival: '',
                departure: '',
                is_paid: false,
                with_breakfast: false
            }
        }),
        mounted() {
            const id = window.location.href.split("/").pop()
            fetch('http://localhost:5000/clients/' + id)
                .then(resp => resp.json())
                .then(data => {
                    this.client = data
                    let arr = formatDate(Date.parse(this.client.arrival))
                    let dep = formatDate(Date.parse(this.client.departure))
                    this.client.arrival = arr
                    this.client.departure = dep
                })
        },
        methods: {
            async editClient(client) {
                client.room_number = +client.room_number
                console.log(client)
                await fetch('http://localhost:5000/clients',
                    {
                        method: 'POST',
                        mode: 'cors',
                        body: JSON.stringify(client),
                        headers: {
                            "Content-Type": "application/json",
                        },
                    })
                    .then(resp => {
                        if (resp.status === 200) {
                            alert('OK')
                        } else {
                            console.log(resp)
                            alert('OOPS!')
                        }
                    }).catch(e => {
                        alert('OOPS!')
                    })
            }
        }
    }

    function formatDate(date) {
        date = new Date(date)
        var day = date.getDate()
        if (day < 10) {
            day = '0' + day
        }
        var monthIndex = date.getMonth() + 1;
        if (monthIndex < 10) {
            monthIndex = '0' + monthIndex
        }
        var year = date.getFullYear();

        return year + '-' + monthIndex + '-' + day;
    }
</script>

<style scoped>

</style>