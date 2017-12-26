/**
 Created by $(USER) on $(DATE)
 **/


gameOfThrones.factory('battleService',['$q', '$http' ,function($q, $http){

    return{


        getBattleList : function(obj){
            return $http.get('http://localhost:4444/battleDetailsDisplay/', {params : obj}).then(function (response) {
                if (response !== undefined && response.data !== undefined) {
                    return response.data;
                }
                else {
                    return $q.reject(response);
                }
            });
        }

    }
}]);