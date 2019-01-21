<template>
    <div class="btn-group btn-group-sm">
        <button class="btn btn-default" @click="editRoom">
            Редактировать
        </button>
        <button class="btn btn-danger" @click="deleteRoom">
            Удалить
        </button>
    </div>
</template>
<script>
    export default {
        props: ['row'],
        methods: {
            deleteRoom() {
                let self = this
                let ok = confirm("Подтвердите удаление.");
                if (!ok) {
                    return
                }
                let url = 'http://localhost:5000/'
                url += self.row.number !== undefined ? 'rooms/' : 'clients/'
                url += self.row.id
                console.log(url)
                fetch(url, {
                    method: 'DELETE',
                    mode: 'cors',
                    headers: {
                        "Content-Type": "application/json",
                    },
                }).then(resp => {
                    if (resp.status === 200) {
                        alert('OK')
                    } else {
                        alert('OOPS!')
                    }
                }).catch(e => {
                    alert('OOPS!')
                })
            },
            editRoom() {
                console.log(this.row.id)
                if (this.row.number !== undefined) {
                    window.location.hash = '#edit-room/' + this.row.id
                } else {
                    window.location.hash = '#edit-client/' + this.row.id
                }
            }
        }
    }
</script>
<style>

</style>