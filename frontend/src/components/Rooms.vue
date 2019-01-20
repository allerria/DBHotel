<template>
    <div>
        <a class="btn-success btn" style="margin-top: 20px" href="#add-room">Добавить номер</a>
        <datatable v-bind="$data"/>
    </div>
</template>
<script>
    export default {
        data: () => ({
            columns: [
                {title: 'ID', field: 'id'},
                {title: 'Номер', field: 'number'},
                {title: 'Кол-во мест', field: 'persons'},
                {title: 'Этаж', field: 'floor'},
                {title: 'ТВ', field: 'has_tv'},
                {title: 'Холодильник', field: 'has_fridge'},
                {title: 'Телефон', field: 'has_phone'},
                {title: 'Цена', field: 'price'},
                {title: 'Цена с завтраком', field: 'price_with_breakfast'}
            ],
            data: [],
            total: 0,
            query: {}
        }),
        mounted() {
            fetch('http://localhost:5000/rooms')
                .then(resp => resp.json())
                .then(datka => {
                    this.data = datka
                })
        }
    }
</script>