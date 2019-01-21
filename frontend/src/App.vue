<template>
    <div>
        <nav class="navbar navbar-default">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">
                    Exam DB
                </a>
            </div>
        </nav>

        <div class="container">
            <ul class="nav nav-tabs nav-justified">
                <li :class="{ active: showTab === 'rooms' }">
                    <a href="#rooms">Rooms</a>
                </li>
                <li :class="{ active: showTab === 'clients' }">
                    <a href="#clients">Clients</a>
                </li>
                <li :class="{ active: showTab === 'incomes' }">
                    <a href="#incomes">Incomes</a>
                </li>
                <li :class="{ active: showTab === 'available' }">
                    <a href="#available">Available rooms</a>
                </li>
                <li :class="{ active: showTab === 'get-room' }">
                    <a href="#get-room">Get room</a>
                </li>
            </ul>
            <div class="tab-content" style="margin-top: 10px">
                <div class="tab-pane" :class="{ active: showTab === 'clients' }">
                    <clients v-if="showTab === 'clients'"/>
                </div>
                <div class="tab-pane" :class="{ active: showTab === 'rooms' }">
                    <rooms v-if="showTab === 'rooms'"/>
                </div>
                <div class="tab-pane" :class="{ active: showTab === 'incomes' }">
                    <incomes v-if="showTab === 'incomes'"/>
                </div>
                <available-rooms v-show="showTab === 'available'"/>
                <get-room v-show="showTab === 'get-room'"/>
                <add-room v-if="showTab === 'add-room'"/>
                <add-client v-if="showTab === 'add-client'"/>
                <edit-room v-if="showTab.startsWith('edit-room')"/>
                <edit-client v-if="showTab.startsWith('edit-client')"/>
            </div>
            <hr/>
        </div>
    </div>
</template>
<script>
    import Clients from './components/Clients'
    import Rooms from './components/Rooms'
    import Incomes from './components/Incomes'
    import AddRoom from './components/AddRoom'
    import AddClient from './components/AddClient'
    import EditRoom from './components/EditRoom'
    import EditClient from './components/EditClient'
    import AvailableRooms from "./components/AvailableRooms";
    import GetRoom from "./components/GetRoom";

    export default {
        components: {
            GetRoom,
            AvailableRooms,
            AddRoom,
            Clients,
            Incomes,
            Rooms,
            AddClient,
            EditRoom,
            EditClient
        },
        data: () => ({
            showTab: getCurHash()
        }),
        mounted() {
            $(window).on('hashchange', () => {
                this.showTab = getCurHash()
                console.clear()
            })
        }
    }

    function getCurHash() {
        // display Advanced example by default
        return location.hash.replace(/^#/, '') || 'rooms'
    }
</script>
<style>
    html {
        position: relative;
        min-height: 100%;
    }

    footer {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        padding: 5px 0;
        font-size: 12px;
        text-align: center;
        color: #afafaf;
    }
</style>