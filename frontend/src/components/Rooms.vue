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
                {title: 'ID', field: 'id', sortable: true},
                {title: 'Номер', field: 'number', sortable: true},
                {title: 'Кол-во мест', field: 'persons', sortable: true},
                {title: 'Этаж', field: 'floor', sortable: true},
                {title: 'ТВ', field: 'has_tv', sortable: true},
                {title: 'Холодильник', field: 'has_fridge', sortable: true},
                {title: 'Телефон', field: 'has_phone', sortable: true},
                {title: 'Цена', field: 'price', sortable: true},
                {title: 'Цена с завтраком', field: 'price_with_breakfast', sortable: true}
            ],
            data: [],
            total: 0,
            query: {}
        }),
        mounted: () => {
            fetch('http://localhost:5000/rooms')
                .then(resp => resp.json())
                .then(data => console.log(data))
        }
    }
</script>