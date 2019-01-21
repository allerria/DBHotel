<template>
    <form>
        <div class="form-group">
            <label>Id</label>
            <input type="number" class="form-control" disabled v-model="room.id">
        </div>
        <div class="form-group">
            <label>Номер</label>
            <input type="number" class="form-control" v-model="room.number">
        </div>
        <div class="form-group">
            <label>Кол-во мест</label>
            <input type="number" class="form-control" v-model="room.persons">
        </div>
        <div class="form-group">
            <label>Этаж</label>
            <input type="number" class="form-control" v-model="room.floor">
        </div>
        <div class="form-group">
            <label>Есть ТВ</label>
            <input type="checkbox" v-model="room.has_tv">
        </div>
        <div class="form-group">
            <label>Есть холодильник</label>
            <input type="checkbox" v-model="room.has_fridge">
        </div>
        <div class="form-group">
            <label>Есть телефон</label>
            <input type="checkbox" v-model="room.has_phone">
        </div>
        <div class="form-group">
            <label>Цена</label>
            <input type="number" class="form-control" v-model="room.price">
        </div>
        <div class="form-group">
            <label>Цена с завтраком</label>
            <input type="number" class="form-control" v-model="room.price_with_breakfast">
        </div>
        <button class="btn btn-primary" @click="editRoom(room)">Submit</button>
    </form>
</template>

<script>
    export default {
        data: () => ({
            room: {
                id: '',
                number: '',
                persons: '',
                floor: '',
                has_tv: false,
                has_fridge: false,
                has_phone: false,
                price: '',
                price_with_breakfast: ''
            }
        }),
        mounted() {
            const id = window.location.href.split("/").pop()
            fetch('http://localhost:5000/rooms/' + id)
                .then(resp => resp.json())
                .then(data => {
                    this.room = data
                })
        },
        methods: {
            editRoom: async (room) => {
                room.number = +room.number
                room.persons = +room.persons
                room.floor = +room.floor
                room.price = +room.price
                room.price_with_breakfast = +room.price_with_breakfast
                console.log(room)
                await fetch('http://localhost:5000/rooms',
                    {
                        method: 'POST',
                        mode: 'cors',
                        body: JSON.stringify(room),
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