<?php
/**
 * Created by PhpStorm.
 * User: dsm2017
 * Date: 2018-10-01
 * Time: 오전 8:57
 */

class Entree
{
    public $name;
    public $ingredients = array(); /* ingredient (명) 재료, 구성 요소 */

    public function hasIngredient($ingredient)
    {
        return in_array($ingredient, $this->ingredients);
    }
}

$soup = new Entree();  // $soup 에 Entree 객체 할당

// $soup 속성 설정
$soup -> name = 'Chicken Soup';
$soup -> ingredients = array('Chicken', 'Water');

$sandwich = new Entree();  // 또 다른 인스턴스 생성 -> $sandwich 에 할당

// $sandwich 속성 설정
$sandwich -> name = 'Chicken Sandwich';
$sandwich -> ingredients = array('Chicken', 'Bread');

foreach (['Chicken', 'Lemon', 'Bread', 'Water'] as $ing)
{
    if ($soup -> hasIngredient($ing))
    {
        echo "Materials to make soup : ". $ing . '<br>';
    }

    if ($sandwich -> hasIngredient($ing))
    {
        echo "Materials to make sandwich : ". $ing . '<br>';
    }
}
