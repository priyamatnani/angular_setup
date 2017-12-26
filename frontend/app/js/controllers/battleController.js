/**
 Created by $(USER) on $(DATE)
 **/


gameOfThrones.controller('battleController',['battleService', function(battleService){

    var self = this;

    /********************************** model *******************************************/

    /********************************** view *******************************************/

    self.selectedIndex = 0;
    /********************************** controller *******************************************/


    function getBattleList(){
        var objToSend = {
            "name" : "battle of the golden tooth"
        };
        battleService.getBattleList(objToSend).then(function(response){
            if(response !== undefined && JSON.stringify(response) !== '{}'){
                console.log(">>>>>>>>>>>>>>",response);
            }
        });
    }

    function initController(){

        getBattleList();
    }

    initController();

}]);