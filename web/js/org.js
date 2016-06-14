angular.module('org', ['btford.markdown', 'ngDialog'])

.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common["X-Requested-With"] = 'XMLHttpRequest';
}])

.controller('Main', function ($scope, $http, ngDialog) {
    $scope.state = Object();
    $scope.branches = Array();
    $scope.branch = Object();
    $scope.cards = Array();

    $scope.get_cards = function () {
        $http.get('/card').then(
            function (r) {
                $scope.cards = r.data.cards;
            },
            function () { alert('Could not get cards!'); }
        );
    };

    $scope.get_card = function (id) {
        $http.get('/card/' + id).then(
            function (r) {
                $scope.cards += r.data;
            },
            function () { alert('Could not get card ' + id + '!'); }
        );
    };

    $scope.open_create_card = function () {
        ngDialog.open({
            template: 'card_form.html',
            data: {
                get_card: $scope.get_card,
            },
            controller: ['$scope', '$http', function ($scope, $http) {
                $scope.create_card = function (title, description) {
                    $http({
                        method: 'POST',
                        url: '/card',
                        data: {
                            title: title,
                            description: description,
                        },
                    }).then(
                        function (r) {
                            $scope.closeThisDialog();
                            $scope.ngDialogData.get_card(r.data.id);
                        },
                        function () { alert('Could not create card :(') }
                    );
                };
            }],
        });
    };

    $scope.rename = function (branch) {
        ngDialog.open({
            template: 'rename_branch_form.html',
            data: {
                branch: branch,
            },
            controller: ['$scope', '$http', function ($scope, $http) {
                $scope.rename_branch = function (new_name) {
                    $http({
                        method: 'PUT',
                        url: '/b/' + branch.root,
                        data: new_name,
                    }).then(
                        function (r) {
                            $scope.closeThisDialog();
                            branch.name = new_name;
                        },
                        function () { alert('Could not create card :(') }
                    );
                };
            }],
        });
    };

    $scope.get_cards();
})


.controller("Card", function ($scope, $http) {
    $scope.load_card = function (card_id) {
        $http.get('/card/' + card_id).then(
            function (r) {
                $scope.card.id = r.id;
                $scope.card.title = r.title;
                $scope.card.description = r.description;
            },
            function () { alert('Could not load card ' + card_id); }
        );
    };

    $scope.load_card($scope.card.key);
});
