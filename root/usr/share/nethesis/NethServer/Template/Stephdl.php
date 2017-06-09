<?php
/* @var $view Nethgui\Renderer\Xhtml */
echo $view->header()->setAttribute('template', $T('Stephdl_header'));

echo $view->panel()
    ->insert($view->textLabel('Explanations_label')->setAttribute('template', $T('Explanations_label')))
    ->insert( $view->panel()->insert($view->literal("<a href='https://mirror.de-labrusse.fr' target='_blank'>https://mirror.de-labrusse.fr</a>")->setAttribute('hsc', FALSE)))
    ->insert($view->textInput('login',$view::LABEL_LEFT))
    ->insert($view->textInput('password', $view::TEXTINPUT_PASSWORD|$view::LABEL_LEFT))
    ->insert($view->textarea('uuid',$view::STATE_READONLY|$view::LABEL_LEFT)->setAttribute('dimensions', '1x40'));

echo $view->buttonList($view::BUTTON_SUBMIT);
