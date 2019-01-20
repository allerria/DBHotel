<template>
    <form>
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
        <button class="btn btn-primary" @click="addClient(client)">Submit</button>
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
        methods: {
            addClient: async (client) => {
                client.room_number = +client.room_number
                console.log(client)
                await fetch('http://localhost:5000/clients',
                    {
                        method: 'PUT',
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
</script>

<style scoped>

</style>