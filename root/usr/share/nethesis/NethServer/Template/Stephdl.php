<?php
/* @var $view Nethgui\Renderer\Xhtml */
echo $view->header()->setAttribute('template', $T('Stephdl_header'));
echo $view->panel()
    ->insert($view->textLabel('Explanations'))
    ->insert($view->textInput('login'))
    ->insert($view->textInput('password'));
echo "<dt>".$T('NethserverID_label')."</dt><dd>"; echo $view->textLabel('uuid'); echo "</dd>";
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
