<template>
    <form>
        <div class="form-group">
            <label>Номер</label>
            <input type="number" class="form-control" v-model="number">
        </div>
        <button class="btn btn-primary" @click="getRoom(number)">Submit</button>
        <div class="form-group">
            <label>Свободно сейчас</label>
            <input type="text" disabled class="form-control" v-model="room.available">
        </div>
        <div class="form-group">
            <label>Кол-во мест</label>
            <input type="number" disabled class="form-control" v-model="room.persons">
        </div>
        <div class="form-group">
            <label>Этаж</label>
            <input type="number" disabled class="form-control" v-model="room.floor">
        </div>
        <div class="form-group">
            <label>Есть ТВ</label>
            <input type="checkbox" disabled v-model="room.has_tv">
        </div>
        <div class="form-group">
            <label>Есть холодильник</label>
            <input type="checkbox" disabled v-model="room.has_fridge">
        </div>
        <div class="form-group">
            <label>Есть телефон</label>
            <input type="checkbox" disabled v-model="room.has_phone">
        </div>
        <div class="form-group">
            <label>Цена</label>
            <input type="number" disabled class="form-control" v-model="room.price">
        </div>
        <div class="form-group">
            <label>Цена с завтраком</label>
            <input type="number" disabled class="form-control" v-model="room.price_with_breakfast">
        </div>
    </form>
</template>

<script>
    export default {
        data: () => ({
            number: '',
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
        methods: {
            async getRoom(number) {
                fetch('http://localhost:5000/rooms/number/' + number)
                    .then(resp => resp.json())
                    .then(data => {
                        if (data === null) {
                            this.room = {
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
                            alert('Нет такого номера')
                            return
                        }
                        this.room = data
                        this.room.available = this.room.available === 0 ? 'Нет' : 'Да'
                        console.log(this.room.available)
                    })
                    .catch(e => {
                    })
            }
        }
    }
</script>

<style scoped>

</style>