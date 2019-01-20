<template>
    <div>
        <a class="btn-success btn" style="margin-top: 20px" href="#add-client">Добавить клиента</a>
        <datatable v-bind="$data"/>
    </div>
</template>
<script>
    export default {
        data: () => ({
            columns: [
                {title: 'ID', field: 'id'},
                {title: 'Имя', field: 'first_name'},
                {title: 'Фамилия', field: 'last_name'},
                {title: 'Номер', field: 'room_number'},
                {title: 'Дата прибытия', field: 'arrival'},
                {title: 'Дата отправления', field: 'departure'},
                {title: 'Оплачено', field: 'is_paid'},
                {title: 'С завтраком', field: 'with_breakfast'},
            ],
            data: [],
            total: 0,
            query: {}
        }),
        mounted() {
            fetch('http://localhost:5000/clients')
                .then(resp => resp.json())
                .then(datka => {
                    this.data = datka
                })
        }
    }
</script>